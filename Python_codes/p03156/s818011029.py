def main():
    n=int(input())
    a,b=map(int,input().split())
    p=map(int,input().split())
    A,B,C = 0,0,0
    for pp in p:
        if pp <= a:
            A += 1
        elif pp <= b:
            B += 1
        else:
            C += 1
    print(min(A,B,C))

if __name__ == "__main__":
    main()