def main():
    from sys import stdin
    input = lambda:stdin.readline().rstrip()
    H,W,K = map(int,input().split())
    S = []
    num_strawberry = [0]*H
    for i in range(H):
        line = list(map(lambda  x: True if x=='#' else False,list(input())))
        S.append(line)
        num_strawberry[i] = line.count(True)
    
    segment = 0
    ans = []
    for i in range(H):
        ans.append([0]*W)
    for i in range(H):

        if num_strawberry[i] != 0:
            segment += 1
            cake = S[i]
            ansline = ans[i]
            num_s = 0
            for j in range(W):
                ansline[j] = segment
                if cake[j] and num_s < num_strawberry[i] -1:
                    num_s += 1
                    segment += 1
    
    determined = -1
    for i in range(H):
        if num_strawberry[i] != 0:
            determined = i
            break
    if determined > 0:
        for i in range(determined):
            ans[i] = ans[determined]
    for i in range(determined+1,H):
        if num_strawberry[i] != 0:
            determined = i
        else:
            ans[i] = ans[determined]



    for line in ans:
        print(*line)


        



main()