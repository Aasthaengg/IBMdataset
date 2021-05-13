N = int(input())
a = list(map(int,input().split()))
al = sorted(set(a),reverse = 1)
ans = []
for i,j in zip(al[:-1],al[1:]):
    ans.append(i-j)
print(sum(ans))