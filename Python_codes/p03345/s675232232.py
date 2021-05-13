A,B,C,K=map(int,input().split())
if abs(A-B>=10**18):
    print('Unfair')
    exit()
print((A-B)*((-1)**(K%2)))