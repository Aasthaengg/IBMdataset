import math
def is_square(N):
    return math.sqrt(N) - int(math.sqrt(N)) == 0

def get_divisor_count(N):
    divisor_count = 0
    for i in range(1,int(math.sqrt(N))+1):
        if N%i == 0:
            divisor_count += 1
    return divisor_count*2 if is_square(N) == False else divisor_count*2 - 1
if __name__ == "__main__":
    N = int(input())
    count = 0
    for i in range(1,N+1,2):
        if get_divisor_count(i) == 8:
            count += 1
    print(count)