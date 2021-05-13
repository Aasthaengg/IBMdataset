n, k = map(int,input().split())
n_list = [0 for i in range(10**5)]

for i in range(n):
    a, b = map(int,input().split())
    n_list[a-1] += b

temp = 0

for i in range(len(n_list)):
    temp += n_list[i]
    if temp >= k:
        print(i+1)
        break
