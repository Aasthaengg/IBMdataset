#AGC26 A問題
#1:連続する文字列ごとに分割する。（もしくは連続する文字列の長さを記録していく）
#2:連続する文字列内で魔法を使い、連続しないようにするためには？　偶数と奇数でどうなるか

def main():
    n = int(input())
    slimes = list(map(int,input().split()))
    length = length_of_sequences(slimes)
    total = 0
    for l in length:
        total += l//2
    print(total)

def length_of_sequences(l):
    length = []
    counter = 1
    for i,slime in enumerate(l):

        if i == 0:
            continue
        if l[i-1] == l[i]:
            counter += 1
        else:
            length.append(counter)
            counter = 1
        if i == len(l)-1:
            length.append(counter)

    return length



if __name__ == '__main__':
    main()
