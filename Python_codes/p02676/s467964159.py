def resolve():
    K = int(input())
    S = input()
    print(S if len(S) <= K else S[:K]+"...")

if '__main__' == __name__:
    resolve()