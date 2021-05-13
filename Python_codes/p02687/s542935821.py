#import time

def main():
    S = input()
    ans = "ABC" if S == "ARC" else "ARC"
    return ans

if __name__ == '__main__':
    #start = time.time()
    print(main())
    #elapsed_time = time.time() - start
    #print("経過時間:{}".format(elapsed_time * 1000) + "[msec]")