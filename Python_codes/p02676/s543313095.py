def main(K, S):
    ans = S
    if len(S) <= K:
        return ans
    else:
        return ans[:K] + '...'

if __name__ == '__main__':
    K = int(input())
    S = input()
    ans = main(K, S)
    print(ans)

