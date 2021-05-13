def main():
    S = input()
    A = [False]*26
    for char in S:
        if A[ord(char) - ord("a")]:
            print("no")
            return
        else:
            A[ord(char) - ord("a")] = True
    print("yes")

main()