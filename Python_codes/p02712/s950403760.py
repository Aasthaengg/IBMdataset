N=int(input())
F=N//3
B=N//5
fb=N//15
S=(N*(N+1))//2
Fizz=(3*F*(F+1))//2
Buzz=(5*B*(B+1))//2
FizzBuzz=(15*fb*(fb+1))//2
print(S-Fizz-Buzz+FizzBuzz)


