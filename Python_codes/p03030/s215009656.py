n = int(input())
sp = [list([i+1]+list(input().split())) for i in range(n)]
sp2 = sorted(sp,key=lambda x:(x[1],-int(x[2])))
[print(ss[0]) for ss in sp2]