A,B=map(int,input().split())

count=0

for i in range(A,B+1):
    i_str=str(i)
    ri_str=i_str[::-1]
    ri=int(ri_str)
    if i==ri:
        count+=1

print(count)