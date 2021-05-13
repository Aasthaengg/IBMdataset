#! python3
# coding:utf-8
 
def main():
    n = int(input())
    ans = [0 for _ in range(n)]
    for x in range(1,100):
        for y in range(1,100):
            for z in range(1,100):
                eq = x**2 + y**2 + z**2 + x*y + y*z + z*x
                if eq < n+1:
                    ans[eq-1]+=1
    for i in ans:   
        print(i)

if __name__ == "__main__":
    main() 