#-*-coding:utf-8-*-
import sys
input=sys.stdin.readline
import numpy as np

def main():
    menu=[]
    np_menu=[]
    [menu.append(int(input())) for _ in range(5)]
    np_menu=np.array(menu)
    s_menu=sorted(np_menu,key=lambda x:x%10)
    time_counter=0
    last_add=0

    for time in s_menu:
        if time % 10 ==0:
            time_counter+=time
        elif last_add==0:
            last_add+=time
        else:
            tmp=10-(time%10)
            time_counter+=time+tmp
    time_counter+=last_add
    print(time_counter)

if __name__=="__main__":
    main()