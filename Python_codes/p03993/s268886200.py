n = int(input())
a_list = list(map(int, input().split()))

cnt = 0
index_list = list(range(0,n,1))

for i in (index_list):
    if a_list[a_list[i]-1] == i+1:
        cnt += 1
print(cnt//2)