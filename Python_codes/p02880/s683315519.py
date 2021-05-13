n=int(input())

ans = "No"
for i in range(1,10):
    if n%i==0 and n//i<10 :
        ans = "Yes"
        break
print( ans )
