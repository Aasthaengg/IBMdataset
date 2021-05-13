import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
 
def main():
    S = readline().strip().decode()
    K = int(readline())
    if S[0] != '1':
        print(S[0])
        return 

    cnt = 0
    for i in S:
        if i == '1':
            cnt += 1
        else:
            break
    if K <= cnt:
        print('1')
    else:
        print(S[cnt])
if __name__ == '__main__':
    main()
