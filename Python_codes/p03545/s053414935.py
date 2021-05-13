def main(A,B,C,D):
    list = [A,B,C,D]

    tmp = ['+','-']


    for i in range(2**3):
        ans = A
        back = []
        for j in range(3):
            if ( (i>>j)&1 ):
                ans += list[j+1]
                back.append(tmp[0])
            else:
                ans -= list[j+1]
                back.append(tmp[1])
        if ans == 7:
            return back

tmp = int(input())
D = tmp%10
tmp = tmp//10
C = tmp%10
tmp = tmp//10
B = tmp%10
tmp = tmp//10
A = tmp%10
back = main(A,B,C,D)
print(str(A)+back[0]+str(B)+back[1]+str(C)+back[2]+str(D)+'=7')
