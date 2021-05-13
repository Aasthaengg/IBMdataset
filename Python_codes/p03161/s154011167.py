
n,k = map(int,input().split())
li = list(map(int,input().split()))

ans = [0]*n
# 地味に遅い
# for i in range(1,n):
#     l = []
#     if k > i:
#         for j in range(i):
#             l.append(abs(li[i]-li[j])+ans[j])
#     else:
#         for j in range(1,k+1):
#             l.append(abs(li[i]-li[i-j])+ans[i-j])
#     ans[i] = min(l)
# print(ans[-1])

for i in range(1,n):
    l = [ abs(li[i]-li[j]) + ans[j] for j in range(max(0,i-k),i)]
    # print(l)
    ans[i] = min(l)
print(ans[-1])