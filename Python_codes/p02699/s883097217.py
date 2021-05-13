import sys
def main():
    S,W=tuple(map(int,sys.stdin.readline().split()))
    print('unsafe') if S<=W else print('safe')
if __name__=='__main__':main()