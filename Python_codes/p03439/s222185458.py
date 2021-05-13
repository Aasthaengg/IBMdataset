def query(seat,m_max,m_min,seat_0):
    print(seat)
    s=input()

    if (seat%2==0 and s==seat_0) or (seat%2==1 and s!=seat_0):
        m_min=seat
        seat=int(0.5*(m_max+seat))
            
    else :
        m_max=seat
        seat=int(0.5*(m_min+seat))

    query(seat,m_max,m_min,seat_0)

n=int(input())
print(0)
query(int(0.5*n), n, 0, input())