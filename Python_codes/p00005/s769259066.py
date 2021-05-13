import sys
def gcd(a,b):
    if b== 0:return a
    return gcd(b,a%b)
def return_lcm(a,b):
    prime = gcd(a,b)
    return prime*(a/prime)*(b/prime)
def solve():
    a = []
    for line in sys.stdin:
        digit_list = line.split(' ')
        new_list = []
        for j in digit_list:
            new_list.append(int(j))
        a.append(new_list)
    for data in a:
        print str(gcd(data[0],data[1])) + ' ' + str(return_lcm(data[0],data[1]))

if __name__ == "__main__":
    solve()