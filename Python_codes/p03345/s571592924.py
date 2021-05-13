def main():
    A,B,C,K=map(int,input().split())
    if abs(A-B) >= 10**18:
        print('Unfair')
    elif K%2:
        print(B-A)
    else:
        print(A-B)

main()