def main():
    N=input()
    K=len(N)
    ans=int(N[0])+(K-1)*9
    if N==N[0]+'9'*(K-1):
        print(ans)
    else:
        print(ans-1)

main()