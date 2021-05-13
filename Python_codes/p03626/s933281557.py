N = int(input())
S1 = input()
S2 = input()

s = sorted(set(S1) | set(S2))

c = [[None, None]] * N
"""
rrB
ggB

r2
r2

"""
cnt = 1
if S1[0] == S2[0]:
    # x
    # x
    cnt = 3 
    i = 1
else:
    # 012
    # xx
    # yy
    cnt = 6
    i = 2

while i < N:
    m = 0
    if S1[i] == S2[i]:
        if S1[i-1] == S2[i-1]:
            # xA
            # xA
            m= 2
        else:
            # xA
            # yA
            m= 1
        i+=1
    else:
        if S1[i-1] == S2[i-1]:
            # xAA
            # xBB
            m= 2
        else:
            # rrAA r,r,r,g,g,g,b,b,b
            # ggBB r,g,b,r,g,b,r,g,b
            #            o   o o    
            m= 3
        i+=2
    cnt = (cnt * m) % 1000000007
    #print(S1[:i])
    #print(S2[:i])
    #print(m, cnt)
    #print()
print(cnt)
