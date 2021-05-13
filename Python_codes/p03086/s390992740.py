def solve():
    S = input()
    N = len(S)
    max_length = 0

    for i in range(N):
        for j in range(N):
            if i+j >= N:
                break
            temp_str = S[i:N-j]
            temp_str = temp_str.replace("A", "")
            temp_str = temp_str.replace("C", "")
            temp_str = temp_str.replace("G", "")
            temp_str = temp_str.replace("T", "")
            if (len(S[i:N-j]) > 0 and temp_str == ""):
                if (len(S[i:N-j]) > max_length):
                    max_length = len(S[i:N-j])

    print(max_length)


if __name__ == "__main__":
    solve()