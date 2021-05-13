S=input()

T=S.replace("x","")
if T!=T[::-1]:
    print(-1)
    exit()

S="*"+S+"*"
U=S[::-1]

a,b=0,0
K=0
for _ in range(len(T)+2):
    old_a,old_b=a,b
    while S[a]=="x":
        a+=1

    while U[b]=="x":
        b+=1

    delta_a=a-old_a
    delta_b=b-old_b

    K+=max(delta_a,delta_b)-min(delta_a,delta_b)

    a+=1
    b+=1
    assert 1

print(K//2)