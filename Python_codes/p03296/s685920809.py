def run_length_compress(string):
    string = string + [-1]
    n = len(string)

    begin = 0
    end = 1
    cnt = 1
    ans = []
    while True:
        if end >= n:
            break
        if string[begin] == string[end]:
            end += 1
            cnt += 1
        else:
            ans.append((cnt, string[begin]))
            begin = end
            end = begin + 1
            cnt = 1

    return ans


n = int(input())
a = list(map(int, input().split()))
a = run_length_compress(a)

ans = 0
for i, j in a:
    ans += i // 2
print(ans)