a,b,k = map(int,input().split())
ans1 = [i for i in range(a,min(a+k,b+1))]
ans2 = [i for i in range(max(b-k+1,a),b+1)]

ans = set(ans1 + ans2)

print(*sorted(ans),sep="\n")