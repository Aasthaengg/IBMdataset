a,b,k=map(int, input().split())
turn=0
while(k>0):
    if turn==0:
        if a%2==1:
            a-=1
        b+=a/2
        a//=2
        turn=1
    else:
        if b%2==1:
            b-=1
        a+=b/2
        b//=2
        turn=0
    k-=1

print("{} {}".format(int(a),int(b)))