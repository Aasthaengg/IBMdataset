n, k = map(int, input().split())
h_list = []
mn = 1e10
for i in range(n) :
    h = int(input())
    h_list.append(h)
h_list.sort()
for i in range(n-k+1) :
    mn = min(mn,(h_list[i+(k-1)]-h_list[i]))
print(mn)
