def main():
    K=int(input())
    S=input()
    if len(S)<=K:
        print(S)
        return
    print(S[:K]+'...')
main()