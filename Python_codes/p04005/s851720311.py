a, b, c = map(int, input().split())

L1 = a*b*(c//2)-a*b*(c-c//2)
L2 = a*(b//2)*c-a*(b-b//2)*c
L3 = (a//2)*b*c-(a-a//2)*b*c
L = [abs(L1), abs(L2), abs(L3)]
print(min(L))
