a = int(input())
b,c = map(int,input().split())
if b<=c-(c%a):
    print("OK")
else:
    print("NG")
