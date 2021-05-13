n,m,k=[int(i) for i in input().split()]
def main():
    for i in range(n+1):
        for j in range(m+1):
            if i*(m-j)+j*(n-i)==k:
                print("Yes")
                return
    print("No")
main()