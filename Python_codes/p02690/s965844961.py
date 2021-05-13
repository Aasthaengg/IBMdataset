#import time

def main():
    X = int(input())
    #print(isprime(int((9**5-5**5)/4)))
    lis = [[ [] for _ in range(240)] for _ in range(240)]
    ansA, ansB = 0, 0
    #print(type(ansA), ansB)
    for i in range (240):
        for j in range(240):
            lis[i][j].append(i-120)
            lis[i][j].append(j-120)
    
    for i in range(240):
        for j in range(240):
            A, B = lis[i][j]
            if A**5 - B**5 == X:
                ansA, ansB = A, B
                break
        else: #普通に終わったら実行される、breakならされない
            continue
        break #外側


    print(ansA, ansB)


if __name__ == '__main__':
    #start = time.time()
    main()
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")