def main(A,B,C):
    if (B // A) > C:
        return C
    else:
        return (B // A)
        
A,B,C = map(int,input().split())
print(main(A,B,C))