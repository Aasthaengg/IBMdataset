N = int(input())
city={}
city_name=[]
for n in range(N):
    S = input().split()
    city[n+1]=S
    city_name.append(S[0])

city_name=list(set(city_name))
city_name.sort()

for c_name in city_name:
    city_temp = {}
    for c_key in city.keys():
        if city[c_key][0] == c_name:
            city_temp[int(city[c_key][1])]=c_key
            
    p_temp = list(city_temp.keys())
    p_temp.sort(reverse=True)
    for v in p_temp:
        print(city_temp[v])