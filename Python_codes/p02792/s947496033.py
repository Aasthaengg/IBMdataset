def main():
    N = int(input())
    # ある数値nについて、n[0]..n[-1]とすると
    # 1~n-1の中のある数値mに対して、n[0]==m[-1]&&n[-1]==m[0]となるようなmがいくつ存在するか調べたい
    # n:1...3 -> m:3...1かつlen(n)>len(m)を満たすもの*2
    # n:3...1 -> m:1...3かつlen(n)>=len(m)を満たすもの*2
    # n:1...1 -> m:1...1かつlen(n)>=len(m)を満たすもの*2
    # 下のパターンで、n[0]==n[-1]のときだけ(n,n)が重複するので-1する
    if N<=9:
        print(N)
    else:
        count = 9
        for n in range(10,N+1):
            n = str(n)
            nlen = len(n)
            if n[-1] == '0':
                continue
            if n[0]<n[-1]:
                tmp = int('1'*(nlen-2)) if nlen>2 else 0
                count += tmp*2
            elif n[0]>n[-1]:
                tmp = int('1'*(nlen-1)) if nlen>2 else 1
                count += tmp*2
            else:
                # 2桁以上(10~)と比較
                tmp = int('1'*(nlen-2))+int(n[1:-1])+1 if nlen>2 else 1
                count += tmp*2-1
                # 1桁(1~9)と比較
                count += 2
        print(count)

main()
