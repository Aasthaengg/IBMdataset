def main():
    S = input()
    K = int(input())
    
    lengths = []
    s = S[0]
    prev = S[0]
    length = 1
    for s in S[1:]:
        if s == prev:
            length += 1
        else:
            lengths.append([prev, length])
            length = 1
        prev = s
    lengths.append([s, length])

    if len(lengths) == 1:
        ans = lengths[0][1] * K // 2
    else:
        if lengths[0][0] == lengths[-1][0]:
            joint_len = lengths[0][1] + lengths[-1][1]
            ans = lengths[0][1] // 2
            ans += sum([i[1]//2 for i in lengths[1:-1]]) * K
            ans += joint_len // 2 * (K-1)
            ans += lengths[-1][1] // 2
        else:
            ans = sum([i[1]//2 for i in lengths]) * K
    print(ans)
main()