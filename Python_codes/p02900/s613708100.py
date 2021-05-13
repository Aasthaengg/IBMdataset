def main():
    import numpy as np
    import math

    A, B = map(int, input().split())
    gcd = int(np.gcd(A, B))

    num_to_search = int(math.sqrt(gcd)) + 1

    def factorize_prime(number):
        RV = [1]
        
        if (number != 1):      
            while (number % 2 == 0):
                number //= 2
                RV.append(2)
            
            for i in range(3, num_to_search + 1):
                if (number % i == 0):
                    while (number % i == 0):
                        number //= i
                        RV.append(i)
        
        if (number != 1):
            RV.append(number)
        
        return(RV)

    
    cnt = factorize_prime(gcd)
    ans = len(set(cnt))
    


    
    print(ans)





if __name__ == '__main__':
    main()


