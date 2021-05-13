S = input()

T = ""

while True:
    T_len = len(T)
    for word in ["dream", "dreamer", "erase", "eraser"]:
        if word + T == S[-1 * len(word + T):]:
            T = word + T
            if T == S:
                print("YES")
                exit()
    if T_len == len(T):
        print("NO")
        exit()
