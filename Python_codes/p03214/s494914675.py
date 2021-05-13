N = int(input())
a_li = list(map(int,input().split()))
a_ave = sum(a_li) / len(a_li)
ans = []
for i in range(N):
    ans.append([abs(a_li[i]-a_ave),i])
print(sorted(ans)[0][1])
