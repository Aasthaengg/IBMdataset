def male_or_female(seat,m_max,m_min,seat_0):
    global seat_check, n_max, n_min
    print(seat)
    s=input()

    if seat%2==0:
        if s==seat_0:
            n_min=seat
            seat=int(0.5*(m_max+seat))
            seat_check=seat
            
        else :
            n_max=seat
            seat=int(0.5*(m_min+seat))
            seat_check=seat
            
    else:
        if s!=seat_0:
            n_min=seat
            seat=int(0.5*(m_max+seat))
            seat_check=seat
        else :
            n_max=seat
            seat=int(0.5*(m_min+seat))
            seat_check=seat


n_max=int(input())
n_min=0

print(0)
seat_zero=input()
seat_check=int(0.5*n_max)

for i in range(19):
    male_or_female(seat_check, n_max, n_min, seat_zero)
