def main(D, T, S):
    time = D//S
    if D%S != 0:
        time += 1
    if time <= T:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    D, T, S = map(int, input().split())
    ans = main(D, T, S)
    print(ans)

