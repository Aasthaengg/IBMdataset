import collections
def main():
    A = str(input())
    c = collections.Counter(A)
    c_list = list(c.items())

    ans = len(A)*(len(A)-1)//2
    for i in range(len(c_list)):
    	ans -= c_list[i][1]*(c_list[i][1]-1)//2

    print(ans+1)

if __name__ == "__main__":
    main()