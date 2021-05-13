def main():
    s = input()

    pre = [1, 0, 0, 0]

    MOD = int(1e9) + 7

    for i in range(len(s)):
        next_ = [pre[0], pre[1], pre[2], pre[3]]
        if s[i] == "A":
            next_[1] += pre[0]
        elif s[i] == "B":
            next_[2] += pre[1]
        elif s[i] == "C":
            next_[3] += pre[2]
        else:
            next_[0] = pre[0] * 3
            next_[1] = pre[1] * 3 + pre[0]
            next_[2] = pre[2] * 3 + pre[1]
            next_[3] = pre[3] * 3 + pre[2]
        for i in range(4):
            next_[i] %= MOD
        pre = next_
    
    print(pre[3])

if __name__ == "__main__":
    main()