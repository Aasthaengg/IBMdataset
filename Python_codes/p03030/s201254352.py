n=int(input())
for v in sorted(list(list(input().split())+[i+1] for i in range(n)),key=lambda x:(x[0],-int(x[1]))):print(v[2])