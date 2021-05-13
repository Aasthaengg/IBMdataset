from collections import deque

n, q = [ int( val ) for val in raw_input( ).split( " " ) ]
processes = deque( )
for i in range( n ):
    name, time = raw_input( ).split( " " )
    processes.append( ( name, int( time ) ) )
  
qsum = 0
output = []
while len( processes ):
    process = processes.popleft( )
    if process[1] <= q:
        qsum += process[1]
        output.append( "{:s} {:d}".format( process[0], qsum ) )
    else:
        processes.append( ( process[0], process[1]- q ) )
        qsum += q
 
print( "\n".join( output ) )