N,D = map(int,input().split())
staff = N//(2*D+1)
if N%(2*D+1)!=0:
    staff += 1
print(staff)