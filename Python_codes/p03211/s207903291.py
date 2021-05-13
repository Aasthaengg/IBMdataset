def main():
    S = str(input())
    t = 0
    diff = 0
    near = 10000
    for i in range(2, len(S)):
        t = int(S[i-2]) * 100 + int(S[i-1]) * 10 + int(S[i])
        if 753 < t:
            diff = t - 753
        else:
            diff = 753 - t
        if near > diff:
            near = diff
    print(near) 
main()  