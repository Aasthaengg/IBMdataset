def main():
    n = int(input())
    primes = get_primenumber(55555)
    out = []
    num = 0
    for prime in primes:
        if prime%5 == 1:
           out.append(prime)
           num += 1
        if n == num:
            print(*out)
            return

def get_primenumber(number):
    prime_list = []
    if number < 2:
        return prime_list
    if number == 2:
        return [2]
    search_list = [2] + list(range(3, number+1, 2))
    while True:
      if search_list[0] > number**0.5:
        prime_list.extend(search_list)
        break
      else:
        head_num = search_list[0]
        prime_list.append(head_num)
        search_list.pop(0)
        search_list = [num for num in search_list if num % head_num != 0]
    return prime_list

        
if __name__ == "__main__":
    main()