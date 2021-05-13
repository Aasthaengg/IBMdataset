def main():
    N = int(input())
    S = input()
    total = 0
    for i in range(len(S) - 2):
        if S[i] + S[i + 1] + S[i + 2] == 'ABC':
            total += 1  
    print(total)
main()